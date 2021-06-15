import React from "react";
import Loading from "./Loading";
import { Grid } from "@material-ui/core";

type ResultHeaderProps = {
  name: string;
  imgUrl: string;
  quotes: string;
};

const ResultHeader = ({ name, imgUrl, quotes }: ResultHeaderProps) => {
  return (
    <div style={{ textAlign: "center" }}>
      <div>
        <h1 className='villain-name bottom'>{name}</h1>
      </div>
      <div>{/* <img src={imgUrl} style={{ objectFit: "cover" }} /> */}</div>
      <Grid
        item
        xs={12}
        style={{ verticalAlign: "center", fontSize: "2rem", fontWeight: "bold", textAlign: "center" }}
      >
        {quotes}
      </Grid>
    </div>
  );
};

ResultHeader.defaultProps = {
  name: "짐 모리아티",
  imgUrl:
    "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe1f0dd89-223b-4236-8e71-3f50d378b46e%2Fdarkknight.jpg?table=block&id=6e52f522-7077-45a1-b4fe-34be07b748c6&width=960&userId=a4e51eef-8052-4c1a-aa01-db7663147cd6&cache=v2",
  quotes: "장미꽃은 빨갛고 제비꽃은 파랗지. 사람은 죽고. 죽는 게 사람들이 하는 일이야.",
};

export default ResultHeader;
