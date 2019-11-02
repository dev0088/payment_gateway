const products = [
  {
    id: 1,
    title: "BALANCIGA",
    titleImageUrl: "",
    images: [require("assets/img/shopping/balenciga.png")],
    summarySpec: "40",
    contact: "info@email.com",
    delivery: "408 Wilshire Blvd",
    paymentMethod: "express_card",
    paymentImage: require("assets/img/payments/express-card.png"),
    shipping: "next day shipping",
    price: "$450",
    buttonColor: "zapBuyBlack"
  },
  {
    id: 2,
    title: "Apple HomePad",
    titleImageUrl: require("assets/img/shopping/applehomepad-title.png"),
    images: [require("assets/img/shopping/applehomepad-1.png"), require("assets/img/shopping/balenciga.png")],
    summarySpec: "OS",
    contact: "info@email.com",
    delivery: "408 Wilshire Blvd",
    paymentMethod: "debit-card",
    paymentImage: require("assets/img/payments/debit-card.png"),
    shipping: "next day shipping",
    price: "$450",
    buttonColor: "zapBuyRed"
  },
  {
    id: 3,
    title: "NET-A-PORTER",
    titleImageUrl: "",
    images: [require("assets/img/shopping/netaporter.png")],
    summarySpec: "36",
    contact: "info@email.com",
    delivery: "408 Wilshire Blvd",
    paymentMethod: "apple-pay",
    paymentImage: require("assets/img/payments/apple-pay.png"),
    shipping: "next day shipping",
    price: "$450",
    buttonColor: "zapBuyBlack"
  },
  {
    id: 4,
    title: "Microsoft",
    titleImageUrl: require("assets/img/shopping/microsoft-title.png"),
    images: [require("assets/img/shopping/microsoft.png")],
    summarySpec: "64G",
    contact: "info@email.com",
    delivery: "408 Wilshire Blvd",
    paymentMethod: "apple-pay",
    paymentImage: require("assets/img/payments/apple-pay.png"),
    shipping: "next day shipping",
    price: "$999",
    buttonColor: "zapBuyBlack"
  }
];

module.exports = {
  products
}