import React, { useState } from "react";
import { RouteComponentProps, withRouter } from "react-router";
import { Grid, Button, Modal } from "@material-ui/core";
import { makeStyles, Theme, createStyles } from "@material-ui/core/styles";
import IndexHeader from "../components/sentiment_test/IndexHeader";

type IndexContainerProps = RouteComponentProps;

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    paper: {
      position: "absolute",
      width: Math.round(window.innerWidth / 2) > 420 ? Math.round(window.innerWidth / 4) : "100%",
      height: Math.round(window.innerHeight / 2),
      left: "50%",
      top: "50%",
      marginLeft: Math.round(window.innerWidth / 2) > 420 ? -Math.round(window.innerWidth / 8) : "-57.5%",
      marginTop: -Math.round(window.innerHeight / 4),
      background: theme.palette.background.paper,
      border: "2px solid #000",
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
      textAlign: "center",
    },
  }),
);

const IndexContainer = ({ history }: IndexContainerProps) => {
  const [open, setOpen] = useState(false);
  const startTest = () => history.push("/question");
  const classes = useStyles();
  const modal = (
    <div className={classes.paper}>
      <div id='simple-modal-title'>
        <img
          src='https://cdn.discordapp.com/attachments/824619467832688701/832288902244204634/1602745073935.jpg'
          style={{ width: "300px", objectFit: "cover" }}
        />
      </div>
      <p id='simple-modal-description'>?????????????????????????</p>
      <Button variant='contained' color='primary' onClick={startTest}>
        테스트 시작하기
      </Button>
    </div>
  );
  return (
    <>
      <IndexHeader />
      <Grid item>
        <Button variant='contained' color='primary' onClick={startTest}>
          테스트 시작하기
        </Button>
      </Grid>
      <Grid item>
        <Button variant='contained' color='primary' onClick={() => setOpen(true)}>
          전 착한 사람인데요?
        </Button>
        <Modal
          open={open}
          onClose={() => setOpen(false)}
          aria-labelledby='simple-modal-title'
          aria-describedby='simple-modal-description'
          style={{ margin: "0 auto" }}
        >
          {modal}
        </Modal>
      </Grid>
    </>
  );
};

export default withRouter(IndexContainer);
