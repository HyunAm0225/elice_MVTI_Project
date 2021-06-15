import React from "react";
import { Grid } from "@material-ui/core";

type VillainRelationProps = {
  partner: string;
  rival: string;
};

const VillainRelation = ({ partner, rival }: VillainRelationProps) => {
  return (
    <>
      <Grid item xs={12}>
        <h3>유사한 빌런</h3>
        <p>{partner}</p>
      </Grid>
      <Grid item xs={12}>
        <h3>상반되는 빌런</h3>
        <p>{rival}</p>
      </Grid>
    </>
  );
};

VillainRelation.defaultProps = {
  partner: "partner",
  rival: "rival",
};

export default VillainRelation;
