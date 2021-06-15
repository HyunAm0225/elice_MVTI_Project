import React from "react";
import { useState, useEffect } from "react";
import { RouteComponentProps, withRouter } from "react-router";
import { Box, Grid, Button, Typography, Popover } from "@material-ui/core";
import PopupState, { bindTrigger, bindPopover } from "material-ui-popup-state";

import Counter from "../components/sentiment_test/Counter";
import Profile from "../components/detail/Profile";
import VillainRelation from "../components/sentiment_test/VillainRelation";
import Result from "../components/detail/Result";

type ResultContainerProps = RouteComponentProps<any>;

const ResultContainer = ({ history }: ResultContainerProps) => {
  console.log("가져왔다!");
  const data = JSON.parse(sessionStorage.getItem("data") || "{}")[0];
  console.log(data);

  const resetTest = () => history.push("/");
  const detailResult = () => history.push(`/introduce`);

  const [anchorEl, setAnchorEl] = React.useState<HTMLButtonElement | null>(null);
  const copy = () => {
    const tmp = document.createElement("textarea");
    document.body.appendChild(tmp);
    tmp.value = "http://elice-kdt-ai-track-vm-da-05.koreacentral.cloudapp.azure.com";
    // tmp.value = "http://localhost:3000";
    tmp.select();
    document.execCommand("copy");
    document.body.removeChild(tmp);
  };

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    copy();
    setAnchorEl(event.currentTarget);
    setTimeout(() => setAnchorEl(null), 1000);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const open = Boolean(anchorEl);
  const id = open ? "simple-popover" : undefined;

  const converter = (arr: Array<any>, origin: any) =>
    arr.map((v: string) => {
      return Math.round(Number(origin[v]) * 10);
    });
  const [varr, uarr] = [Object.keys(data.sentiment).sort(), Object.keys(data.user_sentiment).sort()];
  const [sdata, udata] = [converter(varr, data.sentiment), converter(uarr, data.user_sentiment)];
  console.log(sdata, udata);
  return (
    <Grid item xs={12}>
      <Profile
        name={data.name}
        script={data.best_talk}
        mvti={data.mvti_type}
        imgurl={data.character_img_url}
      />
      <br />
      <Counter cnt={data.count} mvti={data.user_mvti} type={data.count} />
      <Result url={data.wc_url} sdata={sdata} udata={udata} />
      <VillainRelation partner={data.partner} rival={data.rival} />
      <Grid
        container
        direction='column'
        justify='flex-start'
        alignItems='center'
        style={{ marginTop: "10px" }}
      >
        <Grid item xs={12}>
          <Button variant='contained' color='primary' onClick={resetTest}>
            다시하기
          </Button>
        </Grid>
        <Button variant='contained' color='primary' onClick={detailResult}>
          상세보기
        </Button>
        <PopupState variant='popover' popupId='demo-popup-popover'>
          {(popupState: any) => (
            <div>
              {/* <Tooltip title='Copy'> */}
              <Button aria-describedby={id} variant='contained' color='primary' onClick={handleClick}>
                공유하기
              </Button>
              {/* </Tooltip> */}
              <Popover
                {...bindPopover(popupState)}
                id={id}
                open={open}
                anchorEl={anchorEl}
                onClose={handleClose}
                anchorOrigin={{
                  vertical: "bottom",
                  horizontal: "center",
                }}
                transformOrigin={{
                  vertical: "top",
                  horizontal: "center",
                }}
              >
                <Box p={2}>
                  <Typography>클립보드에 복사되었습니다</Typography>
                </Box>
              </Popover>
            </div>
          )}
        </PopupState>
      </Grid>
    </Grid>
  );
};

export default withRouter(ResultContainer);
