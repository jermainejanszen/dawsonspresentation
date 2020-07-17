import React from 'react';
import { footerStyle } from './styles';

export class Footer extends React.Component {
    render() {
        return (
            <div style={footerStyle.comp}>
                <h3 style={footerStyle.order}>ORDER ONLINE</h3>
                <h3 style={footerStyle.link} >www.dawsonsespresso.com.au</h3>
            </div>
        );
    }
}