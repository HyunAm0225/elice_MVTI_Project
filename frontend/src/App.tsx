import React from "react";
import { Route, Switch, Redirect } from "react-router-dom";
import Index from "./pages/Index";
import Result from "./pages/Result";
import Questions from "./pages/Questions";
import Detail from "./pages/Detail";
import Intro from "./pages/Intro";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "./App.css";

function App() {
  return (
    <>
      <Switch>
        <Route exact path='/' component={Index} />
        <Route path='/result' component={Result} />
        <Route path={["/question", "/question:@question_id"]} component={Questions} />
        <Route path={["/detail", "/detail:@detail_id"]} component={Detail} />
        <Route path='/introduce' component={Intro} />
      </Switch>
    </>
  );
}

export default App;
