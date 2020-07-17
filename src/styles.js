
export const generalStyle = {
    comp: {
        fontFamily: "Arial, Helvetica, sans-serif",
        //border: "3px solid rgb(0,0,255)",
        padding: "0px 20px",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-around",
        alignContent: "space-around",
        height: "100%",
    }
}

export const headerStyle = {
    comp: {
        //border: "3px solid rgb(0,255,0)",
    },
    image: {
        filter: "invert(100%)",
        padding: "5px 15px",
        maxWidth: "20%",
        float: "left",
    },
    text: {
        textAlign: "center",
    }
}

export const specialStyle = {
    comp: {
        //border: "3px solid rgb(0,255,255)",
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between",
    },
    image: {

    },
    name: {
        fontWeight: "bold",
    },
    desc: {
        color: "rgb(88,88,88)",
        fontWeight: "normal",
        fontStyle: "italic",
    },
    price: {
        fontWeight: "bold",
        float: "right",
        textAlign: "center",
    }
}

export const footerStyle = {
    comp: {
        //border: "3px solid rgb(255,0,0)",
        bottom: 0,
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
    },
    link: {
        padding: "0px 5px",
    },
    order: {
        color: "red",
        padding: "0px 5px",
    }
}