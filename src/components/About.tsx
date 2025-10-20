import React from 'react';
import { CheckCircle } from 'lucide-react';

const aboutPoints = [
  "Transform negative thinking into positive energy",
  "Develop resilience and mental strength",
  "Create a personalized positive thinking practice",
  "Learn techniques from certified positive thinking coaches",
  "Join a supportive community of like-minded individuals"
];

const About = () => {
  return (
    <section id="about" className="py-16 bg-white">
      <div className="container px-4 md:px-6">
        <div className="grid gap-10 lg:grid-cols-2 items-center">
          <div className="flex flex-col justify-center space-y-6">
            <div className="inline-block rounded-full bg-accent/10 px-3 py-1 text-sm font-medium text-accent w-fit">
              About Str8PositiveThinking
            </div>
            <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">
              Your Guide to a <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">Positive Mindset</span>
            </h2>
            
            <p className="text-muted-foreground">
              Str8PositiveThinking was founded with a simple mission: to help people transform their lives through the power of positive thinking. 
              Our founder experienced firsthand how changing thought patterns can lead to extraordinary life changes.
            </p>
            
            <p className="text-muted-foreground">
              Today, we've helped thousands of people overcome negative thought patterns and embrace a more positive, fulfilling life. 
              Our science-based approach combines traditional wisdom with modern psychological insights.
            </p>
            
            <div className="space-y-3">
              {aboutPoints.map((point, index) => (
                <div key={index} className="flex items-start gap-2">
                  <CheckCircle className="h-6 w-6 text-primary flex-shrink-0" />
                  <p>{point}</p>
                </div>
              ))}
            </div>
          </div>
          
          <div className="relative">
            <div className="absolute -top-6 -left-6 w-24 h-24 bg-primary/20 rounded-full blur-xl"></div>
            <div className="absolute -bottom-6 -right-6 w-32 h-32 bg-secondary/20 rounded-full blur-xl"></div>
            
            <div className="relative rounded-2xl overflow-hidden border-8 border-white shadow-xl bg-gradient-to-br from-primary/5 via-secondary/5 to-accent/5 p-10">
              <div className="flex flex-col items-center justify-center text-center space-y-6">
                <div className="w-24 h-24 rounded-full bg-primary/10 flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="text-primary"><circle cx="12" cy="12" r="5"/><path d="M12 1v2"/><path d="M12 21v2"/><path d="m4.2 4.2 1.4 1.4"/><path d="m18.4 18.4 1.4 1.4"/><path d="M1 12h2"/><path d="M21 12h2"/><path d="m4.2 19.8 1.4-1.4"/><path d="m18.4 5.6 1.4-1.4"/></svg>
                </div>
                <h3 className="text-2xl font-bold">Our Mission</h3>
                <p className="text-muted-foreground">
                  At Str8PositiveThinking, we believe that a positive mindset is the foundation for a fulfilling life. 
                  Our mission is to help you discover your inner strength through practical positive thinking techniques.                 
                </p>
                <div className="mt-4">
                  <p className="font-bold text-lg">Founded in 2015</p>
                  <p className="text-sm text-muted-foreground">Helping thousands transform their lives</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;