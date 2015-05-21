# queries for excel spreadsheets
query_list = {
    'deliver_all': """
       SELECT
            a.name  advertiser_name,
            CONCAT('IO: ', CAST(io.id AS CHAR))   io_id,
            c.id   campaign_id,
            c.name campaign_name,
            bsh.budget_date,
            bsh.hour,
            bsh.impressions,
            COALESCE(concat(cm.firstname, ' ', cm.lastname),'*** OWNER NOT FOUND ***') AS owner,
            bsh.timezone
        FROM
            marketplace.campaigns c
        JOIN marketplace.advertisers a                  ON c.advertiser_id = a.id
        JOIN marketplace.line_item_campaign lic         ON lic.campaign_id = c.id
        JOIN marketplace.line_items li                  ON lic.line_item_id = li.id
        JOIN marketplace.insertion_orders io            ON li.io_id = io.id
        LEFT JOIN marketplace.members cm                ON cm.id = io.campaign_manager_id
        JOIN marketplace.budget_stats_hourly bsh        ON c.id = bsh.campaign_id
        WHERE c.start_date < now()
            AND c.end_date > now()
        ORDER BY
            campaign_id,
            campaign_name,
            bsh.budget_date,
            bsh.hour;
    """,

    'too_fast': """
        SELECT
            a.name  advertiser_name,
            CONCAT('IO: ', CAST(io.id AS CHAR))   io_id,
            c.id   campaign_id,
            c.name campaign_name,
            bsh.budget_date,
            bsh.hour,
            bsh.impressions,
            coalesce(concat(cm.firstname, ' ', cm.lastname),'*** OWNER NOT FOUND ***') AS owner,
            bsh.timezone
        FROM
            marketplace.campaigns c
        JOIN marketplace.advertisers a                  ON c.advertiser_id = a.id
        LEFT JOIN marketplace.budget_stats b        ON b.campaign_id = c.id
        JOIN marketplace.line_item_campaign lic     ON lic.campaign_id = c.id
        JOIN marketplace.line_items li              ON li.id = lic.line_item_id
        JOIN marketplace.insertion_orders io        ON io.id = li.io_id
        LEFT JOIN marketplace.members cm  ON cm.id = io.campaign_manager_id
        JOIN marketplace.budget_stats_hourly bsh    ON bsh.campaign_id = c.id
        WHERE c.start_date < now()
            AND c.end_date > now()
            AND b.day_impressions >= 0.9 * c.daily_impressions_cap
            AND DATE(b.budget_date) = DATE(convert_tz(now(), 'UTC', b.timezone))
        ORDER BY
            campaign_id,
            campaign_name,
            budget_date,
            hour;
        """,
    'too_slow': """
        SELECT
            a.name  advertiser_name,
            CONCAT('IO: ', CAST(io.id AS CHAR))   io_id,
            c.id   campaign_id,
            c.name campaign_name,
            bsh.budget_date,
            bsh.hour,
            bsh.impressions,
            coalesce(concat(cm.firstname, ' ', cm.lastname),'*** OWNER NOT FOUND ***') AS owner,
            bsh.timezone
        FROM
            marketplace.campaigns c
        JOIN marketplace.advertisers a                  ON c.advertiser_id = a.id
        LEFT JOIN marketplace.budget_stats b        ON b.campaign_id = c.id
        JOIN marketplace.line_item_campaign lic     ON lic.campaign_id = c.id
        JOIN marketplace.line_items li              ON li.id = lic.line_item_id
        JOIN marketplace.insertion_orders io        ON io.id = li.io_id
        LEFT JOIN marketplace.members cm  ON cm.id = io.campaign_manager_id
        JOIN marketplace.budget_stats_hourly bsh    ON bsh.campaign_id = c.id
        WHERE c.start_date < now()
            AND c.end_date > now()
            AND b.day_impressions <= 0.2 * c.daily_impressions_cap
            AND DATE(b.budget_date) = DATE(convert_tz(now(), 'UTC', b.timezone))
        ORDER BY
            campaign_id,
            campaign_name,
            budget_date,
            hour;
        """
}