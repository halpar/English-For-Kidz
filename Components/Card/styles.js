import styled from "styled-components";

export default styled.div`
  margin: ${({ margin, theme }) => margin && theme.card.margin};
  padding: ${({ padding, theme }) => padding && theme.card.padding};
  
  border-radius: ${({ theme }) => theme.card.borderRadius};
  border-bottom: ${({ color, theme }) => {
    if (color)
      switch (color) {
        case "primary":
          return `3px solid ${theme.main.primaryColor}`;
        case "secondary":
          return `3px solid ${theme.main.secondaryColor}`;
        default:
          return `3px solid ${color}`;
      }
  }};

  background: ${({ background, theme }) => background || theme.card.background};
  ${({ linear }) =>
    linear.length > 0 &&
    `background: linear-gradient(to right, ${linear.join(",")});`}

  color: ${({ background, linear }) =>
    (background || linear.length > 0) && "white"};
  box-shadow: ${({ theme }) => theme.main.shadow};
  word-break: break-word;

  overflow-x: ${({ overflowX }) => overflowX || "auto"};
  overflow-y: ${({ overflowY }) => overflowY || "auto"};
  transition: box-shadow 0.2s cubic-bezier(0.25, 0.8, 0.25, 1);

  &:hover {
    cursor: ${({ onClick }) => onClick && "pointer"};
    box-shadow: ${({ hover, theme }) => hover && theme.main.shadowHover};
  }

  &.full-height{
    
    @media (min-width: 992px) {
    margin-bottom:0px;
    margin-top:0px;
    height:100%;
      }
  }
 &.flex-column{
   display:flex;
   flex-direction:column;
 }
 &.align-center{
  align-items:center;

 }
 &.text-center {
   p , div {
     text-align:justify;
   }
  }

  &.fixed-card-supporters {
   position:fixed;
   width:100%;
   z-index:1000;
  }
  .card-cover {
    width:100%;
    height: 200px;
    object-fit: cover;
    position: fixed;
  }
  
  
`;
