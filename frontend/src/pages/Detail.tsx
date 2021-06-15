import React, { useState, useEffect } from "react";
// import Profile from "../components/detail/Profile";
// import Result from "../components/detail/Result";
import PageTemplate from "../components/PageTemplate";
import DetailContainer from "../containers/DetailContainer";

type DetailProps = {};

const Detail = ({}: DetailProps) => {
  return (
    <PageTemplate>
      <DetailContainer />
    </PageTemplate>
  );
};

Detail.defaultProps = {};

export default Detail;
