import React from 'react';
import { headerStyle } from './styles';

export class Header extends React.Component {
    render() {
        return (
            <div style={headerStyle.comp}>
                <img 
                    src="http://www.dawsonsespresso.com.au/wp-content/uploads/2014/05/light-large.png" 
                    alt="Dawson's Espresso"
                    style={headerStyle.image}
                />
                <h1 style={headerStyle.text}>
                    TODAY'S SPECIALS
                </h1>
            </div>
        );
    }
}