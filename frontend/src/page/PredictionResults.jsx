import { CLASS_NAMES } from "../constants";
import "../styles/PredictionResults.css";
import { useState, useEffect } from "react";
import { useLocation} from "react-router-dom";
import { Card } from "react-bootstrap";
import axios from "axios";

const PredictionResults = () => {

    const location = useLocation();
    const [ diseaseInfo, setDiseaseInfo] = useState(null);
    const formData = new FormData();
    const apiUrl = "http://localhost:3000";

    useEffect(() => {
        const fetchDiseaseData = async () => {
        try {
            const response = await axios.get(`${apiUrl}/disease/${location.state.predictionData.prediction}`);
            setDiseaseInfo(response.data)
            console.log(diseaseInfo)
        } catch (error) {
            console.log(error)
        }
    };
    fetchDiseaseData();
    }, [location.state.predictionData.prediction]);

    if (!diseaseInfo) {
        return <p>Loading...</p>;
}
    
    return (

        <div className="prediction-page">
            <div className="page-title">
                <h1 className="diagnosis-header">Plant Disease Identified!</h1>
                <h1 className="diagnosis">{CLASS_NAMES[location.state.predictionData.prediction]}</h1>
            </div>

            <div className="diagnosis-body">
                <div className="image-section">
                    <img src={location.state.imageUrl} alt="disease" />
                </div>

                {/* <div className="disease-info-section">
                    <h2>{CLASS_NAMES[location.state.predictionData.prediction]} Information</h2>
                </div> */}

                <Card className = "disease-info-section">
                    <Card.Body>
                        <Card.Title className="card-title">
                            {CLASS_NAMES[location.state.predictionData.prediction]}
                        </Card.Title>

                        <Card.Subtitle className="card-subtitle">
                            Disease Name
                        </Card.Subtitle>
                        <Card.Text className="card-text">
                            {CLASS_NAMES[location.state.predictionData.prediction]}
                        </Card.Text>

                        <Card.Subtitle className="card-subtitle">
                            Disease Type
                        </Card.Subtitle>
                        <Card.Text className="card-text">
                            {diseaseInfo.type}
                        </Card.Text>

                        <Card.Subtitle className="card-subtitle">
                            Disease Description
                        </Card.Subtitle>
                        <Card.Text className="card-text">
                            {diseaseInfo.description}
                        </Card.Text>

                        <Card.Subtitle className="card-subtitle">
                            Treatment Advice
                        </Card.Subtitle>
                        <Card.Text className="card-text">
                            {diseaseInfo.treatment}
                        </Card.Text>
                    </Card.Body>
                </Card>
                
            </div>
        </div>

        
       
    )
}

export default PredictionResults;