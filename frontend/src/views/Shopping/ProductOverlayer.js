import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import Modal from '@material-ui/core/Modal';
// local components
import Product from "./Product.js";
import { products } from "variables/products.js";
import styles from "assets/jss/material-dashboard-pro-react/views/productOverlayerStyle.js";


const useStyles = makeStyles(styles);

export default function ProductOverlayer({open, productId, onClose}) {
  const classes = useStyles();

  return (
    <Modal
      aria-labelledby="simple-modal-title"
      aria-describedby="simple-modal-description"
      open={open}
      onClose={onClose}
      className={classes.modalContainer}
    >
      <div className={classes.modalPaper}>
        <Product product={products[productId]} />
      </div>
    </Modal>
  );
}
