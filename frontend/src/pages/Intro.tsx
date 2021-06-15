import { ImportExportOutlined } from "@material-ui/icons";
import React from "react";
import PageTemplate from "../components/PageTemplate";
import IntroContainer from "../containers/IntroContainer";
// import ProfileCard from "../components/detail/ProfileCard";
ImportExportOutlined;
type IntroProps = {};

const Intro = () => {
  return (
    <PageTemplate>
      <IntroContainer />
    </PageTemplate>
  );
};

Intro.defaultProps = {};

export default Intro;
