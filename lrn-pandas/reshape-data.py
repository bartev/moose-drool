idf = event_counts.set_index(['install_date', 'play_date', 'app_client_ver', 'uid', 'event'])

new_df = idf.unstack('event')

new_df.to_csv('wide.csv')


tuples = zip(*[['bar', 'bar', 'baz', 'baz',
			'foo', 'foo', 'qux', 'qux'],
   			['one', 'two', 'one', 'two',
   			'one', 'two', 'one', 'two']]) 

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = DataFrame(randn(8, 2), index=index, columns=['A', 'B'])

df2 = df[:4]

new_df = idf.unstack('event')


x = range(10)
y = ['a', 'b'] * 5
z = [10, 20, 30, 40, 50] * 2
d = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yza', 'bcd']
event = ['login', 'start', 'quit', 'login', 'start', 'quit', 'start', 'login', 'start', 'quit']
freq = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

dummy = pd.DataFrame({'x': x, 'y':y, 'z':z, 'd':d, 'event':event, 'freq':freq})

dummy = pd.DataFrame({'y':y, 'z':z, 'd':d, 'event':event, 'freq':freq})

wd = pd.pivot_table(dummy, values='freq', rows=['y', 'z', 'd'], cols=['event']).fillna(0)

wd = pd.pivot_table(ec, values='freq', rows=['install_date', 'play_date', 'app_client_ver_install', 'uid'], cols='event')


def get_uid_summaries(grp):
    quests = grp['last_quest_cname'].unique()
    num_quests = len(quests)
    if 'i0' in quests: num_quests = num_quests - 1
    num_days_played = len(grp['play_date'].unique())
    sources = grp['source'].unique()
    source = sources[0] if pd.notnull(sources[0]) else 'Organic'
    device_memTotal = grp['device_memTotal'].unique()[0]  # ok to have nulls
    num_repeated_quests = max(0, grp['quest_repeat'].sum())
    num_events_total = grp.shape[0]
    total_time_sec = max(0, grp['mod_dur_seconds'].sum())
    num_quests_won = max(0, grp.sum()['quest_won'])
    num_quests_lost = len((grp[(grp['event'] == 'quest_end') & (grp['quest_won'] == 0)]).index)
    masked_day0 = grp[grp['days_since_install'] == 0]
    day0_total_time_sec = max(0, masked_day0['mod_dur_seconds'].sum())
    day0_num_quests_won = max(0, masked_day0.sum()['quest_won'])
    day0_num_quests_lost = len((masked_day0[(masked_day0['event'] == 'quest_end') & (masked_day0['quest_won'] == 0)]).index)
    
    return pd.Series({'num_quests' : num_quests, 
    	'num_days_played' : num_days_played,
    	'source' : source,
    	'device_memTotal' : device_memTotal,
    	'num_repeated_quests' : num_repeated_quests,
    	'num_events_total' : num_events_total,
    	'total_time_sec' : total_time_sec,
    	'num_quests_won' : num_quests_won,
    	'num_quests_lost' : num_quests_lost,
    	'day0_total_time_sec' : day0_total_time_sec,
    	'day0_num_quests_won' : day0_num_quests_won,
    	'day0_num_quests_lost' : day0_num_quests_lost
    	})

grouped = df.groupby('uid')
res = grouped.apply(get_uid_summaries)


run bv-functions.py
res = get_acquis_events(2)
df_res = xform_acquis_list(res)
tmp = df_res[['uid', 'event_ts', 'quest_won', 'event', 'quest_repeat', 'last_quest_cname']]

mask = [x in ['quest_start', 'quest_end'] for x in tmp['event']]
tmp = tmp[mask]

grouped = tmp.groupby(['uid', 'last_quest_cname'])
qcnts = grouped.size().reset_index()
qcnts.columns = ['uid', 'quest', 'freq']
q1 = qcnts[qcnts['freq'] > 3]
q2 = tmp[tmp['uid'] == q1.ix[5][0]]
q2.to_csv('q2.csv')




def get_day_summaries(df, days_since_install):
	mask = df['days_since_install'] == days_since_install
	df0 = df[mask].copy()
	prefix = 'day_' + str(days_since_install) + '_'
	grouped = df0.groupby(['uid', 'event'])
	event_counts = grouped
	
	def fn(grp):
		num_repeated_quests = max(0, grp['quest_repeat'].sum())
		







def count_per_uid_events(df_acquis_data):
	""" return a wide data frame with event counts """
	gb_cols = ['install_date', 
				'play_date',
				'days_since_install',
				'app_client_ver_install', 
				'uid', 
				'event', 
				'new_event']
	df_to_count = df[gb_cols].copy()
	grouped = df_to_count.groupby(['install_date', 'play_date', 'days_since_install', 'app_client_ver_install', 'uid', 'event'])
	event_counts = grouped.size().reset_index()
	grouped = df_to_count.groupby(['install_date', 'play_date', 'days_since_install', 'app_client_ver_install', 'uid', 'new_event'])
	new_event_counts = grouped.size().reset_index()
	new_colnames = ['install_date', 'play_date', 'days_since_instal', 'app_client_ver_install', 'uid', 'event', 'freq']
	event_counts.columns = new_colnames
	new_event_counts.columns = new_colnames
	event_counts = event_counts.append(new_event_counts).drop_duplicates()
	wd = pd.pivot_table(event_counts, 
			values='freq', 
			rows=['install_date', 'play_date', 'app_client_ver_install', 'uid'], 
			cols='event').reset_index().fillna(0)

	grouped = df.groupby('uid')
	res = grouped.apply(get_uid_summaries).reset_index()
	wd = pd.merge(wd, res, on='uid', how='outer')
	# TODO merge wd & res
	return wd
