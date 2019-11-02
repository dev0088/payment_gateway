import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import Button from "components/CustomButtons/Button.js";
import ProductItem from "./ProductItem.js";
import styles from "assets/jss/material-dashboard-pro-react/views/productStyle.js";

const useStyles = makeStyles(styles);

export default function ProductOverlayer({product}) {
  const classes = useStyles();

  return (  
    <GridContainer className={classes.productContainer} >
      <GridItem xs={12}>
        <GridContainer className={classes.productTitleContainer}>
          <GridItem xs={3} />
          <GridItem xs={6} style={{margin: "auto"}}>
            { product.titleImageUrl === "" ? (
              <div className={classes.title}>{product.title}</div>
            ) : (
              <div className={classes.titleImageContainer}>
                <img src={product.titleImageUrl} alt="..." className={classes.titleImage} />
              </div>
            )}
          </GridItem>
          <GridItem xs={3} style={{textAlign: 'right'}}>
            <img src={require("assets/img/faces/avatar.jpg")} alt="..." className={classes.avatar}/>
          </GridItem>
        </GridContainer>
      </GridItem>

      
      <GridItem xs={12}>
        <GridContainer className={classes.productionImageContainer}>
          <GridItem lg={4} md={3} xs={12} />
          <GridItem  lg={4} md={6} xs={12} >
            <div className={classes.imgContainer}>
              <img src={product.images[0]} alt="..." className={classes.img} />
            </div>
          </GridItem>
          <GridItem lg={4}  md={3} xs={12}  style={{marginTop: "auto"}}>
            <div className={classes.specValue}>
              {product.summarySpec}
            </div>
          </GridItem>
        </GridContainer>
      </GridItem>

      <GridItem xs={12}>
        <ProductItem title="contact" value={product.contact} cost="" />
      </GridItem>

      <GridItem xs={12}>
        <ProductItem title="delivery" value={product.delivery} cost="" />
      </GridItem>

      <GridItem xs={12}>
        <ProductItem
          title="payment"
          value={
            <div className={classes.imgContainer}>
              <img src={product.paymentImage} alt="..." className={classes.paymentImage} />
            </div>
          }
          cost=""
          valueType="image"
        />
      </GridItem>

      <GridItem xs={12}>
        <ProductItem title="shipping" value={product.shipping} cost="" />
      </GridItem>

      <GridItem xs={12}>
        <ProductItem title="price" value="" cost={product.price} />
      </GridItem>

      <GridItem xs={12}>
        <ProductItem
          title=""
          value={
            <Button color={product.buttonColor}>
              <div>Buy Now</div>
            </Button>
          }
          cost=""
        />
      </GridItem>

    </GridContainer>
  );
}
