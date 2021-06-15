import React from "react";
import Grid from "@material-ui/core/Grid";

type ProfileProps = {
  name: string;
  script: string;
  mvti: string;
  imgurl: string;
};

const label = [
  {
    N: "부정",
    P: "긍정",
  },
  {
    S: "비애형",
    J: "쾌락형",
  },
  {
    A: "분노형",
    T: "신뢰형",
  },
  {
    F: "근심형",
    A: "기대형",
  },
];

const Profile = ({ name, script, mvti, imgurl }: ProfileProps) => {
  // const mvti_arr = mvti.split("").reduce((acc, cur, id) => {
  //   acc
  // })
  return (
    <Grid item xs={12}>
      <h1 className='villain-name bottom'>{name}</h1>
      <h2 className='mvti'>{mvti}</h2>
      <Grid item xs={12}>
        <img style={{ width: "100%", objectFit: "cover" }} src={imgurl} />
      </Grid>
      <Grid
        item
        xs={12}
        style={{ verticalAlign: "center", fontSize: "2rem", fontWeight: "bold", textAlign: "center" }}
      >
        {script}
      </Grid>
    </Grid>
  );
};

Profile.defaultProps = {
  name: "스노우볼",
  script: "장미는 빨갛고 제비꽃은 파랗지. 사람은 죽고. 죽는게 사람들이 하는 일이야.",
  mvti: "MVTI",
  imgurl:
    "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb7439e9e-fc74-452f-b605-08535cdefebb%2FUntitled.png?table=block&id=7b108a0f-0746-4245-a86a-c908423d1775&width=900&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
};

export default Profile;
