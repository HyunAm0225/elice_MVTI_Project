import React from "react";
import { RouteComponentProps, withRouter, Link } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles({
  root: {
    maxWidth: 345,
  },
});

type ProfileCardProps = {
  name: string;
  imgurl: string;
};

const ProfileCard = ({ name, imgurl }: ProfileCardProps) => {
  const classes = useStyles();
  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          component='img'
          alt='Contemplative Reptile'
          height='200'
          image={imgurl}
          title='Contemplative Reptile'
        />
        <CardContent>
          <h2 style={{ margin: 0 }}>{name}</h2>
          {/* <Typography variant='body2' color='textSecondary' component='p'>
            Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all
            continents except Antarctica
          </Typography> */}
        </CardContent>
      </CardActionArea>
      <CardActions style={{ display: "block", margin: 0 }}>
        <Button size='small' color='primary'>
          <Link
            to={`/detail/${name}`}
            type='button'
            className='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary'
          >
            <span className='MuiButton-label'>자세히 보기 🔍</span>
            <span className='MuiTouchRipple-root'></span>
          </Link>
        </Button>
      </CardActions>
    </Card>
  );
};

ProfileCard.defaultProps = {
  name: "Snowball",
  imgurl:
    "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb7439e9e-fc74-452f-b605-08535cdefebb%2FUntitled.png?table=block&id=7b108a0f-0746-4245-a86a-c908423d1775&width=900&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
};

export default ProfileCard;
