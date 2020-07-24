
const testSpecials = {
    date: "1-1-2020",
    specials: [
        {
            key: "1",
            name: "Pesto Chicken Wrap",
            desc: "lettuce, tomato, aioli, pesto, parmesan & chips",
            price: "11.00"
        },
        {
            key: "2",
            name: "Salt & Pepper Squid",
            desc: "with salad & chips",
            price: "11.00"
        },
        {
            key: "3",
            name: "Outback Burger",
            desc: "marinated beef patty, caramelised onion, spinach, bush tomato relish & cheese with BBQ sauce & chips",
            price: "11.00"
        }
    ]
};

export const getSpecials = () => {
    
    const specials = testSpecials;
    
    return specials;
}