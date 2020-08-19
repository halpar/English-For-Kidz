import styled from "styled-components";
import { Carousel } from "antd";

export default styled(Carousel)`
  width: 100%;
  max-width: 80vw;

  /* buttons */
  li > button {
    background: ${({ theme }) => theme.main.secondaryColor} !important;
  }

  .carousel-img {
    width: 100%;
    max-height: 500px;
    object-fit: cover;
  }

  .slick-dots {
    
    li {
      height: 16px !important;
      &.slick-active {
        height: 24px !important;
      }
      button {
        height: 100% !important;
        border-radius: 50% !important;
        margin: 75px;
        margin-left: auto;
        margin-right: auto;
      }
      button-bottom {
        height: 100% !important;
        border-radius: 50% !important;
        margin-left: auto;
        margin-right: auto;
      }
    }
  }
`;
