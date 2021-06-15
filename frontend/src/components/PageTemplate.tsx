import React, { useEffect } from "react";
import { loadCSS } from "fg-loadcss";
import { Grid, Container, Typography, Link } from "@material-ui/core";
import Icon from "@material-ui/core/Icon";
import { makeStyles, createStyles, Theme } from "@material-ui/core/styles";

type PageTemplateProps = {
  children?: React.ReactChild | React.ReactChild[];
};

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    color: {
      backgroundColor: "white",
    },
    box: {
      height: "100%",
      width: "100%",
      boxShadow: "3",
      marginTop: "5px",
      padding: "3px",
    },
  }),
);

const PageTemplate = ({ children }: PageTemplateProps) => {
  const classes = useStyles();
  React.useEffect(() => {
    const node = loadCSS(
      "https://use.fontawesome.com/releases/v5.12.0/css/all.css",
      document.querySelector("#font-awesome-css") as HTMLElement,
    );

    return () => {
      node.parentNode!.removeChild(node);
    };
  }, []);
  return (
    <Container maxWidth='xs'>
      <Grid container direction='column' justify='flex-start' alignItems='center' className={classes.color}>
        <Grid item xs />
        <Grid
          container
          direction='column'
          justify='center'
          alignItems='center'
          className={classes.box}
          spacing={3}
        >
          {children}
        </Grid>
        <Grid item xs />
        <Grid item xs={12} style={{ marginTop: "50px" }}>
          Movie Villain Type Indicator
          <Typography variant='body2' color='textSecondary' align='center'>
            {"Copyright © "}
            <Link
              color='inherit'
              href='https://kdt-gitlab.elice.io/001-part3-moviecharacter/team5/project-MVTI'
            >
              <Icon className='fab fa-gitlab' style={{ fontSize: "1em" }} />
              &nbsp;Gitlab Project-MVTI&nbsp;
            </Link>{" "}
            {new Date().getFullYear()}
            {"."}
          </Typography>
        </Grid>
      </Grid>
    </Container>
  );
};

PageTemplate.defaultProps = {
  children: <>{"출력 오류"}</>,
};

export default PageTemplate;
