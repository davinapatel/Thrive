import { CLASS_NAMES } from "../constants";
import { useEffect, useState } from "react";
import { Card, Row, Col} from "react-bootstrap";
import axios from "axios";
import "../styles/Tracker.css"

const Tracker = () => {

  const [previousPredictions, setPreviousPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const apiUrl = "http://localhost:3000";

    useEffect(() => {
        const fetchPreviousPredictions = async () => {
            try{
                const response = await axios.get(`${apiUrl}/userpredictions/${1}`)
                console.log(response.data.Records)
                setPreviousPredictions(response.data.Records);
            } catch (error) {
                console.log(error)
            } finally {
              setLoading(false);
            }

        };
        fetchPreviousPredictions();
    }, []);

    return (
      <div className="tracker-page">
        <div className="tracker-page-title">
          <h1 className="tracker-header">Previous Plant Diagnoses</h1>
          <h2 className="tracker-subtext">Here are the previous plant diagnoses you've made with Thrive.</h2>
        </div>

        {loading && <p> Loading previous diagnoses...</p>}
        {!loading && previousPredictions.length === 0 && <p>No previous diagnoses made.</p>}
        {!loading && previousPredictions.length > 0 && (
        <Row className="tracker-row flex-wrap">
          {previousPredictions.map((prediction, index) => {
            // Remove "api/" prefix from image path if present
            const imagePath =  `${apiUrl}/${prediction.image.replace(/^api\//, "")}`

            return (
              <Col key={index} className="tracker-col-auto">
                <Card className="tracker-card mb-3">
                  <Card.Img
                    variant="top"
                    src={imagePath}
                    className = "tracker-card-image"
                  />
                  <Card.Body>
                    <Card.Title className="tracker-card-title">
                      {CLASS_NAMES[prediction.prediction]}
                    </Card.Title>
                    <Card.Text className="tracker-card-date">
                      Date:{" "}
                      {new Date(prediction.date).toLocaleDateString("en-GB")}
                    </Card.Text>
                  </Card.Body>
                </Card>
              </Col>
            );
          })}
        </Row>
        )}
      </div>
    );
};


export default Tracker;