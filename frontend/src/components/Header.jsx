import React from "react";
import "./Header.css";
import logo from "../images/logo.jpg"

const Header =() => {
    return (
        <header className="header">
            <div className="logo-section">
                <img src={logo} alt="Thrive Logo" className="logo" /> 
                <h1 className = "company-name">Thrive</h1>
            </div>
            
            <nav className="navigation-links">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/diagnose">Disease Diagnosis</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;