import Home from "./page/Home";
import Diagnose from "./page/Diagnose";
import PredictionResults from "./page/PredictionResults";
import Tracker from "./page/Tracker";
import Header from "./components/Header";
import { Routes, Route} from "react-router-dom";
import "./styles/App.css"

function App() {

    return (
        <>
        <div className="d-flex flex-column min-vh-100">
            <Header />
            <div className="flex-grow-1 d-flex justify-content-center align-items-center">
                    <Routes>
                        <Route path = "/" element = {<Home />} />
                        <Route path = "/diagnose" element= {<Diagnose />} />
                        <Route path="/prediction" element={<PredictionResults />} />
                        <Route path ="/tracker" element={<Tracker />} />
                    </Routes>
                
            </div> 
        </div>
        </>
    );
}

export default App;