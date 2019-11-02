import {
  defaultFont
} from "assets/jss/material-dashboard-pro-react.js";

const productStyle = theme => ({
  productContainer: {
    display: 'contents',
  },
  productTitleContainer: {
    paddingBottom: '50px!important'
  },
  title: {
    fontFamily: defaultFont.fontFamily,
    fontWeight: '700',
    fontSize: 25,
    textAlign: 'center'
  },
  titleImageContainer: {
    textAlign: 'center'
  },
  titleImage: {
    // width: 60
  },
  avatar: {
    width: 50,
    borderRadius: '50%'
  },
  productionImageContainer: {
    paddingBottom: '20px!important'
  },
  imgContainer: {
    
  },
  img: {
    width: 224,
    // height: 585
  },
  paymentImage: {
    width: 100
  },
  specValue: {
    textAlign: 'right',
    fontWeight: 600
  }
});

export default productStyle;
