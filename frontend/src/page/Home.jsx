import "../styles/Home.css";
import home from "../images/home-image.jpg";

const Home = () => {
    return (

        <div className="home-page">
            <div className="home-title">
                <h1 className="home-header">Welcome to Thrive</h1>
                <p>Understand your plants better with Thrive</p>
                <p>Use our AI-Powered tools to identify plant diseases and wild mushrooms in your garden.</p>
                <p>Let's keep your plants thriving!</p>

                <div className="howto-section">
                    <h2 className="instructions-header">How to use Thrive</h2>
                    <div className="howto-item">
                        <span className="howto-number">1.</span> Upload a photo of your plant or mushroom
                    </div>
                    <div className="howto-item">
                        <span className="howto-number">2.</span> AI tool analyzes the image to detect diseases or identify mushroom species
                    </div>
                    <div className="howto-item">
                        <span className="howto-number">3.</span> Receive results with diagnosis and treatment tips if needed
                    </div>
                </div>
            </div>

            <div className="home-image">
                <img src={home} alt="Home Image - Magnifier glass on plants" className="home" /> 
            </div>

        </div>
          
    );
};

export default Home
