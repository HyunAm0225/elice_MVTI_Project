import React, { useState, useEffect, useRef } from "react";
import { Grid } from "@material-ui/core";
import { Radar } from "react-chartjs-2";
import WordCloud from "wordcloud";

type ResultProps = {
  url?: string;
  sdata?: Array<number>;
  udata?: Array<number>;
  type: number;
};

const labels = [
  "anger",
  "anticipation",
  "disgust",
  "fear",
  "joy",
  "negative",
  "positive",
  "sadness",
  "surprise",
  "trust",
];

const Result = ({ url, sdata, udata, type }: ResultProps) => {
  const data = {
    labels,
    datasets: [
      {
        label: "Villain Sentiment",
        backgroundColor: "rgba(29, 38, 113, 0.2)",
        borderColor: "rgba(29, 38, 113, 1)",
        pointBackgroundColor: "rgba(29, 38, 113, 1)",
        pointBorderColor: "#fff",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgba(29, 38, 113, 1)",
        data: sdata,
      },
    ],
  };

  const tdata = {
    labels,
    datasets: [
      {
        label: "Villain Sentiment",
        backgroundColor: "rgba(29, 38, 113, 0.2)",
        borderColor: "rgba(29, 38, 113, 1)",
        pointBackgroundColor: "rgba(29, 38, 113, 1)",
        pointBorderColor: "#fff",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgba(29, 38, 113, 1)",
        data: sdata,
      },
      {
        label: "My Sentiment",
        backgroundColor: "rgba(195, 55, 100,0.2)",
        borderColor: "rgba(195, 55, 100,1)",
        pointBackgroundColor: "rgba(195, 55, 100,1)",
        pointBorderColor: "#fff",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgba(195, 55, 100,1)",
        data: udata,
      },
    ],
  };
  console.log(tdata);
  return (
    <>
      <Grid item xs={12}>
        <p>감정 분석표</p>
        <Radar
          data={type === 1 ? data : tdata}
          width={600}
          height={300}
          options={{
            responsive: true,
            maintainAspectRatio: false,
          }}
        />
      </Grid>
      {type === 1 ? (
        <Grid item xs={12}>
          <p>Word Cloud</p>
          <img src={url} style={{ width: "100%", objectFit: "cover" }} />
          {/* <canvas ref={myCanvas}></canvas> */}
        </Grid>
      ) : null}
    </>
  );
};

Result.defaultProps = {
  url:
    "https://kdt-gitlab.elice.io/001-part3-moviecharacter/team5/project-MVTI/-/raw/master/data-analytics/visualization/wordCloudImgs/Fletcher.png",
  type: 0,
  sdata: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  udata: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
};

export default Result;
