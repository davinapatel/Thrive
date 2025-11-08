import Home from "./page/Home";
import { Routes, Route } from "react-router-dom";

function App() {

    return (
        <>
        <div className="d-flex flex-column min-vh-100">
            <Routes>
                <Route path = "/" element = {<Home />} />
            </Routes>
        </div>
        </>
    );
}

export default App;