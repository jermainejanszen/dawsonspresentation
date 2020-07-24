
export const generalStyle = {
    comp: {
        fontFamily: "Arial, Helvetica, sans-serif",
        border: "3px solid rgb(0,0,255)",
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
        border: "3px solid rgb(0,255,0)",
        display: "flex",
        alignContent: "center",
    },
    image: {
        filter: "invert(100%)",
        padding: "5px 15px",
        maxWidth: "20%",
    },
    text: {
        textAlign: "center",
        flexGrow: 1,
    }
}

export const specialListStyle = {
    border: "3px solid rgb(255,0,255)",
    flexGrow: 1,
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-around",
}

export const specialStyle = {
    comp: {
        border: "3px solid rgb(0,255,255)",
        flexGrow: 1,
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between",
        alignContent: "center",
    },
    image: {
        padding: "0.5%",
        borderRadius: "5%",
        width: "auto",
        height: "80%",
    },
    text: {
        flexGrow: 1,
        padding: "2%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
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
        padding: "2%",
        fontWeight: "bold",
        textAlign: "center",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
    }
}

export const footerStyle = {
    comp: {
        border: "3px solid rgb(255,0,0)",
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