import React, { useState, useEffect } from "react";
import axios from "axios";
import { useLocation } from "react-router-dom";
import { Grid } from "@material-ui/core";
import Profile from "../components/detail/Profile";
import Result from "../components/detail/Result";

type DetailContainerProps = {};

axios.defaults.headers["Access-Control-Allow-Origin"] = "*";

const getVillains = (name: string) =>
  axios({
    method: "get",
    url: `/api/character/${name}`,
  });

const DetailContainer = ({}: DetailContainerProps) => {
  const path = useLocation().pathname.split("/");
  const cname = path[path.length - 1];
  const [villain, setVillain] = useState<any>({
    id: 0,
    name: "",
    wc_url: "",
    bar_url: "",
    best_talk: "",
    character_img_url: "",
    mvti_type: "",
    partner: "",
    rival: "",
    sentiment: [],
  });

  const { name, wc_url, best_talk, character_img_url, mvti_type, partner, rival, sentiment } = villain;

  const arr = Object.keys(sentiment).sort();
  const sdata = arr.map((v: string) => {
    console.log(v);
    return Math.round(Number(sentiment[v]) * 100);
  });

  useEffect(() => {
    getVillains(cname).then((res) => {
      console.log(res.data);
      setVillain(res.data);
    });
  }, []);

  return (
    <Grid item xs={12}>
      <Profile name={name} script={best_talk} mvti={mvti_type} imgurl={character_img_url} />
      <Result url={wc_url} sdata={sdata} />
    </Grid>
  );
};

DetailContainer.defaultProps = {};

export default DetailContainer;
