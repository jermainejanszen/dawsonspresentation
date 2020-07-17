import React from 'react';
import PropTypes from 'prop-types';
import { specialStyle } from './styles';

export class Special extends React.Component {
    render() {
        return (
            <div style={specialStyle.comp}>
                <div>
                    <h2 style={specialStyle.name}>{this.props.name}</h2>
                    <h3 style={specialStyle.desc}>{this.props.desc}</h3>
                </div>
                <h2 style={specialStyle.price}>{this.props.price}</h2>
            </div>
        );
    }
}

Special.propTypes = {
    key: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    desc: PropTypes.string.isRequired,
    price: PropTypes.string.isRequired
}