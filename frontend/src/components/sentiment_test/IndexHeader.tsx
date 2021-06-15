import React from "react";
import { Grid } from "@material-ui/core";
import ImageSlider from "./ImageSlider";

const IndexHeader = () => {
  return (
    <Grid item xs={12}>
      <h1>MVTI</h1>
      <p>나 는 어 떤 빌 런 유 형 일 까 ? 😈</p>
      <ImageSlider />
      <Grid item xs={12} style={{ margin: "30px" }} />
      {/* <img
        src={imgUrl}
        style={{ width: "400px", height: "inherit", objectFit: "cover", objectPosition: "50% 50%" }}
      /> */}
    </Grid>
  );
};

export default IndexHeader;
