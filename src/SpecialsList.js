import React from 'react';
import { Special } from './Special';
import { getSpecials } from './scraper/scraper';
import { specialListStyle } from './styles';

export class SpecialsList extends React.Component {

    render() {
        const specials = getSpecials();
        var specialComps = [];
        specials.specials.forEach(value => {
            specialComps.push(
                <Special 
                    key={value.id} 
                    name={value.name} 
                    desc={value.desc} 
                    price={value.price} 
                />
            )
        });

        return (
            <div style={specialListStyle}>
                {specialComps}
            </div>
        );
    }
}