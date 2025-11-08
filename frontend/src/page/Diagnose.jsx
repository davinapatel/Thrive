import { useState } from "react";
import "../styles/Uploader.css";
import { MdCloudUpload, MdDelete } from "react-icons/md";
import { AiFillFileImage } from "react-icons/ai";
import { Button } from "react-bootstrap";
import axios from "axios";

const Diagnose = () => {
  const [image, setImage] = useState(null);
  const [imageFile, setImageFile] = useState(null);
  const [imageFileName, setImageFileName] = useState("No selected file");
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const apiUrl = "http://localhost:3000";


  const handlePlantDiagnosis = async () => {

    if (imageFile === null) {
        console.log("Need to provide an image to make a prediction");
        return;
    }

    const formData = new FormData();
    formData.append("file", imageFile)

    try {
        setLoading(true)
        const response = await axios.post(apiUrl + "/predict", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        });

        setPrediction(response.data.prediction);
    } catch (error) {
        console.log(error)
    } finally {
        setLoading(false);
    }

  }

  return (
    <div className="diagnose-page">

      <h1 className = "title"> Plant Disease Diagnosis</h1>
      <p className="help-text">Upload an image of the plant leaf you would like to identify the disease for.</p>

      <main className="uploader-main">
        <form
          className="upload-form"
          onClick={() => document.querySelector(".input-field").click()}
        >
          <input
            type="file"
            accept="image/*"
            className="input-field"
            hidden
            onChange={({ target: { files } }) => {
              if (files && files[0]) {
                setImageFile(files[0]);
                setImageFileName(files[0].name);
                setImage(URL.createObjectURL(files[0]));
                setPrediction(null);
              }
            }}
          />

          {image ? (
            <div className="image-preview">
              <img src={image} alt={imageFileName} />
            </div>
          ) : (
            <MdCloudUpload color="#000000" size={60} />
          )}
        </form>

        <section className="uploaded-row">
          <AiFillFileImage color="#000000" />
          <span className="upload-content">
            {imageFileName}
            <MdDelete
              onClick={() => {
                setImageFileName("No selected file");
                setImage(null);
                setImageFile(null);
              }}
            />
          </span>
        </section>
      </main> 

      <Button className="diagnose-button" onClick={handlePlantDiagnosis}>{loading ? "Diagnosing...":"Diagnose Plant!"}</Button>
      

      { prediction && (
        <p className="prediction-result">
            <strong>Prediction:</strong> {prediction}
        </p>
      )}
    </div>
  );
};

export default Diagnose;
