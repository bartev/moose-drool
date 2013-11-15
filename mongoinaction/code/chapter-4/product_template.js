doc =
{ _id: new ObjectId("4c4b1476238d3b4dd5003981"),
  slug: "wheel-barrow-9092",
  sku: "9092",
  name: "Extra Large Wheel Barrow",
  description: "Heavy duty wheel barrow...",

  details: {
    weight: 47,
    weight_units: "lbs",
    model_num: 4039283402,
    manufacturer: "Acme",
    color: "Green"
  },

  total_reviews: 4,
  average_review: 4.5,

  pricing:  {
    retail: 589700,
    sale: 489700,
  },

  price_history: [
      {retail: 529700,
       sale: 429700,
       start: new Date(2010, 4, 1),
       end: new Date(2010, 4, 8)
      },

      {retail:  529700,
       sale:  529700,
       start: new Date(2010, 4, 9),
       end: new Date(2010, 4, 16)
      },
  ],

  category_ids: [new ObjectId("6a5b1476238d3b4dd5000048"),
                    new ObjectId("6a5b1476238d3b4dd5000049")],

  main_cat_id: new ObjectId("6a5b1476238d3b4dd5000048"),

  tags: ["tools", "gardening", "soil"],

}
