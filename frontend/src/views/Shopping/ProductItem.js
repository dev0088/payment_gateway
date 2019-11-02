import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import styles from "assets/jss/material-dashboard-pro-react/views/productItemStyle.js";

const useStyles = makeStyles(styles);

export default function ProductItem({title, value, cost, valueType}) {
  const classes = useStyles();

  return (
    <GridContainer
      style={{
        paddingTop: 15,
        paddingBottom: 15
      }}
    >
      <GridItem xs={4} style={{margin: "auto"}}>
        <div className={classes.title}>{title}</div>
      </GridItem>
      <GridItem xs={4}>
        <div className={classes.value}>{value}</div>
      </GridItem>
      <GridItem xs={4}>
        <div className={classes.cost}>{cost}</div>
      </GridItem>
    </GridContainer>
  );
}
