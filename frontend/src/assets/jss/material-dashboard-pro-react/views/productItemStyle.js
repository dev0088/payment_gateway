import {
  defaultFont
} from "assets/jss/material-dashboard-pro-react.js";

const productItemStyle = theme => ({
  container: {
    height: 30
  },
  title: {
    fontFamily: "Sofia Pro Semi",
    textAlign: "left"
  },
  value: {
    fontFamily: "Sofia Pro Semi",
    textAlign: "center"
  },
  cost: {
    fontFamily: "Sofia Pro",
    textAlign: "right",
    fontWeight: 500
  }
});

export default productItemStyle;
