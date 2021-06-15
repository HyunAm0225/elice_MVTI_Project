import React, { useState, useRef, useEffect } from "react";
import { RouteComponentProps, withRouter, Redirect } from "react-router";

import axios from "axios";
import { Grid, Button } from "@material-ui/core";

import Loading from "../components/sentiment_test/Loading";
import QuestionHeader from "../components/sentiment_test/QuestionHeader";
import ProgressBar from "../components/sentiment_test/ProgressBar";
import type { question } from "../data/QuestionList";
import questionList from "../data/QuestionList";

type QuestionContainerProps = RouteComponentProps;

const QuestionContainer = ({ history }: QuestionContainerProps) => {
  const currentId = useRef<number>(0);
  const [question, setQuestion] = useState(questionList["questionList"][0]);
  const [results, setResults] = useState<Array<string>>([]);

  useEffect(() => {
    if (results.length === 10) {
      const data = { words: results };
      axios({
        method: "post",
        url: "http://elice-kdt-ai-track-vm-da-05.koreacentral.cloudapp.azure.com:8000/api/sentiment/",
        data,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "POST, GET, PUT, DELETE, OPTIONS",
          "Access-Control-Allow-Headers": "*",
          "Access-Control-Max-Age": 86400,
        },
      }).then((res) => {
        console.log("전송 성공");
        const data = [res.data];
        sessionStorage.setItem("data", JSON.stringify(data));
        console.log("보냈다!");
        history.push("/result");
      });
    }
  }, [results.length]);
  const changeQuestion = async (type: string) => {
    currentId.current += 1;
    setQuestion(questionList["questionList"][currentId.current]);
    addResults(type);
  };

  const addResults = (type: string) => {
    setResults([...results, type]);
  };
  console.log(results);
  const sentenceItems =
    currentId.current >= 10
      ? []
      : questionList["questionList"][currentId.current]["options"].map((option: Array<string>, i: number) => (
          <Grid container direction='column' justify='flex-start' alignItems='center'>
            <Button key={i} variant='contained' color='primary' onClick={() => changeQuestion(option[0])}>
              {option[1]}
            </Button>
            &nbsp;
          </Grid>
        ));
  return (
    <Grid item>
      {results.length === 10 ? (
        <>
          <Loading />
        </>
      ) : (
        <>
          <ProgressBar stepIndex={currentId.current} /> <QuestionHeader question={question} />
        </>
      )}
      {sentenceItems}
    </Grid>
  );
};

export default withRouter(QuestionContainer);
