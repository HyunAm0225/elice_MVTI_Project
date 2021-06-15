import React, { useState, useEffect } from "react";
import Slider from "react-slick";

const imageList = [
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe1f0dd89-223b-4236-8e71-3f50d378b46e%2Fdarkknight.jpg?table=block&id=6e52f522-7077-45a1-b4fe-34be07b748c6&width=960&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2c06d1d6-faea-429a-878c-00d31631a801%2Ffrozen.jpeg?table=block&id=646886b6-52fc-4915-8c44-b3c8c055b4bf&width=2500&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F660719af-8a20-4bfd-b459-d2d2a02bb4d0%2FUntitled.png?table=block&id=449baf43-ba5e-44b8-a9e8-795d8fe654d6&width=1510&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0d2a8fa4-c807-41a0-acef-6984bdacdc26%2FUntitled.png?table=block&id=e1af9839-59a8-4da7-83ad-a7a228c6f84f&width=1020&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fde57c919-b9b8-4a10-a5da-f27974a86376%2FUntitled.png?table=block&id=291baaa2-1505-4fa0-b089-657a238f8437&width=1020&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://t1.daumcdn.net/cfile/tistory/990FD4425D28595303",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F37481d0e-cecb-4c90-9273-09c202ea95a4%2Fthanos.jpg?table=block&id=87b2e024-029e-4d80-b3a2-8c362717e726&width=1520&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4c52531f-cc56-4892-8017-921cbf646bea%2Fstarwars.jpg?table=block&id=d181eb75-8d32-4632-b2a0-424e2d4f6610&width=950&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffbac66f2-e649-43d4-8993-f62ba6bad155%2Fhannibal.jpg?table=block&id=f9467575-49ce-40e7-a4fa-60c09bd7b7d6&width=1300&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd72e31d0-4fee-4a00-83ef-996e34c573fd%2Fscar.jpg?table=block&id=ff6dec7c-be78-4cc6-b340-25cb0c7b30f3&width=1340&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fddd00567-6401-40ab-bd57-fdb79ac571d6%2Fharleyquinn.jpg?table=block&id=8a3d913d-7d8f-49ce-96dd-9cb7e8a3608f&width=1160&userId=479b5c03-3ace-4f65-938c-026795f1021d&cache=v2",
  "https://lh3.googleusercontent.com/proxy/JjJJapm7AZEPt_N1Gfu-fUD2CqKPDzZ5Nh754hSVDX-TZkHtuqh0XWLZvvp71aj9UyuS1Nwk5VB7-Hao5KaOWNPrH7OEHPt1E_Q-7BZP_od7QXIfqAh8Osu823vWbxAlatdotsi8GGJqbPezd7RwWdgQp1c-HSmUEu-uRdDf0rvS-PvSMTjpVl7e6A",
];

const ImageSlider = () => {
  const [settings, setSettings] = useState({
    dots: window.innerWidth > 420 ? true : false,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
  });

  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  const handleResize = () => {
    setWindowSize({
      width: window.innerWidth,
      height: window.innerHeight,
    });

    windowSize.width <= 420
      ? setSettings({ ...settings, dots: false })
      : setSettings({ ...settings, dots: true });
  };

  useEffect(() => {
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  });

  return (
    <Slider {...settings}>
      {imageList.map((img, i) => (
        <div key={i} style={{ width: "800px", height: "300px" }}>
          <img src={img} style={{ width: "500px", height: "300px", objectFit: "cover" }} />
        </div>
      ))}
    </Slider>
  );
};

export default ImageSlider;
