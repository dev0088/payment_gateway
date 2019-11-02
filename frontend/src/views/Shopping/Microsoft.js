import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";

// core components
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";

import styles from "assets/jss/material-dashboard-pro-react/views/balanciaStyle.js";

import product1 from "assets/img/shopping/microsoft.png";
import ProductOverlayer from "./ProductOverlayer.js";

const useStyles = makeStyles(styles);

export default function Microsoft() {
  const [open, setOpen] = React.useState(true);
  const classes = useStyles();

  return (
    <GridContainer>
      <div className={classes.imgContainer} onClick={() => setOpen(true)}>
        <img src={product1} alt="..." className={classes.img} />
      </div>
      <ProductOverlayer open={open} productId={3} onClose={() => {setOpen(false)}} />
    </GridContainer>
  );
}
