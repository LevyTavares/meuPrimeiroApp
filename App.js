// App.js
import React, { useState, useEffect } from 'react';
import SplashScreen from './SplashScreen';
import HomeScreen from './HomeScreen';
import CreateTemplateScreen from './CreateTemplateScreen';
import ReportsScreen from './ReportsScreen';
import CorrectorScreen from './CorrectorScreen';

export default function App() {
  const [currentScreen, setCurrentScreen] = useState('splash');
  const [templates, setTemplates] = useState([]); 

  useEffect(() => {
    const timer = setTimeout(() => setCurrentScreen('home'), 2500);
    return () => clearTimeout(timer);
  }, []);

  const handleAddTemplate = (title, numQuestoes, correctAnswers) => {
    const newTemplate = {
      id: Date.now().toString(),
      title: title,
      date: new Date().toLocaleDateString('pt-BR'),
      numQuestoes: parseInt(numQuestoes, 10),
      correctAnswers: correctAnswers, 
      results: [], 
    };
    setTemplates(prevTemplates => [newTemplate, ...prevTemplates]);
  };

  // ===== MUDANÇA PRINCIPAL AQUI =====
  // 1. A função agora aceita matrícula e turma
  const handleAddReport = (template, result, studentName, studentMatricula, studentTurma) => {
    setTemplates(prevTemplates => {
      return prevTemplates.map(t => {
        if (t.id === template.id) {
          const newResult = {
            id: Date.now().toString(), 
            studentName: studentName || 'Aluno Não Identificado',
            // 2. Salva os novos dados
            studentMatricula: studentMatricula || 'Não informada', 
            studentTurma: studentTurma || 'Não informada',
            ...result,
          };
          return { ...t, results: [newResult, ...t.results] };
        }
        return t;
      });
    });
  };
  
  const navigate = (screen) => setCurrentScreen(screen);

  switch (currentScreen) {
    case 'splash':
      return <SplashScreen />;
    case 'home':
      return <HomeScreen onNavigate={navigate} />;
    case 'createTemplate':
      return <CreateTemplateScreen onNavigate={navigate} onAddTemplate={handleAddTemplate} />;
    case 'reports':
      return <ReportsScreen onNavigate={navigate} templates={templates} />;
    case 'corrector':
      return <CorrectorScreen onNavigate={navigate} templates={templates} onAddReport={handleAddReport} />;
    default:
      return <HomeScreen onNavigate={navigate} />;
  }
}