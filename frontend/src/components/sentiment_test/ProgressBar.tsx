import React from "react";
import { makeStyles, useTheme } from "@material-ui/core/styles";
import MobileStepper from "@material-ui/core/MobileStepper";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles({
  root: {
    flexGrow: 1,
  },
});

type ProgressMobileStepperProps = {
  stepIndex: number;
};

export default function ProgressMobileStepper({ stepIndex }: ProgressMobileStepperProps) {
  const classes = useStyles();
  const theme = useTheme();

  return (
    <MobileStepper
      variant='progress'
      steps={11}
      position='static'
      activeStep={stepIndex}
      className={classes.root}
      nextButton={<Button disabled={true} />}
      backButton={<Button disabled={true} />}
    />
  );
}
