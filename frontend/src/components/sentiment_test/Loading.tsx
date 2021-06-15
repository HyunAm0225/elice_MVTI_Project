import React, { useState, useEffect } from "react";
import { CircularProgress } from "@material-ui/core";

type LoadingProps = {
  success: boolean;
};

const Loading = ({ success }: LoadingProps) => {
  const [comma, setComma] = useState<string>("");
  //   const loading = setInterval(() => {
  //     comma.length === 3 ? setComma("") : setComma(comma + ".");
  //   }, 2000);
  //   useEffect(() => {
  //     loading;
  //     return () => clearInterval(loading);
  //   });
  return (
    <div>
      <CircularProgress style={{ color: "#c33764" }} />
      <h1>빌런 매칭을 진행중입니다{comma}</h1>
    </div>
  );
};

Loading.defaultProps = {
  success: true,
};

export default Loading;
