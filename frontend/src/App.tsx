import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import MissionControl from './pages/MissionControl';
import GeoSynthesis from './pages/GeoSynthesis';
import Simulate from './pages/Simulate';
import HindcastValidation from './pages/HindcastValidation';
import ThreatMatrix from './pages/ThreatMatrix';
import './styles/globals.css';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/mission-control" replace />} />
        <Route path="/mission-control" element={<MissionControl />} />
        <Route path="/geo-synthesis" element={<GeoSynthesis />} />
        <Route path="/simulate/:cityId" element={<Simulate />} />
        <Route path="/hindcast-validation" element={<HindcastValidation />} />
        <Route path="/threat-matrix" element={<ThreatMatrix />} />
      </Routes>
    </BrowserRouter>
  );
}
