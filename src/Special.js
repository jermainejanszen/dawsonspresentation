import React from 'react';
import PropTypes from 'prop-types';
import { specialStyle } from './styles';

export class Special extends React.Component {
    render() {
        const imagePath = "/images/" + this.props.id.toString() + ".gif";
        return (
            <li key={this.props.id} style={specialStyle.comp} >
                <img src={imagePath} alt={this.props.id} style={specialStyle.image} />
                <div style={specialStyle.text}>
                    <h2 style={specialStyle.name}>{this.props.name}</h2>
                    <h3 style={specialStyle.desc}>{this.props.desc}</h3>
                </div>
                <h2 style={specialStyle.price}>{this.props.price}</h2>
            </li>
        );
    }
}

Special.propTypes = {
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    desc: PropTypes.string.isRequired,
    price: PropTypes.string.isRequired
}