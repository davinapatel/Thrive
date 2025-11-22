import "../styles/Header.css";
import { Link } from "react-router-dom";
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
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/diagnose">Disease Diagnosis</Link>
                    </li>
                    <li>
                        <Link to="/tracker">Disease Tracker</Link>
                    </li>
                    <li>
                        <Link to="/contact">Contact</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;