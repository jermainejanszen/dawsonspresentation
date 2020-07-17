import React from 'react';
import { Header } from './Header';
import { Footer } from './Footer';
import { SpecialsList } from './SpecialsList';
import { generalStyle } from './styles';

export class Presentation extends React.Component {
    render() {
        return (
            <div style={generalStyle.comp}>
                <Header />
                <SpecialsList />
                <Footer />
            </div>
        );
    }
}