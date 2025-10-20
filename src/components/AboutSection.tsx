import React from "react";
import { Badge } from "@/components/ui/badge";
import { CheckCircle, Sparkles } from "lucide-react";

const aboutPoints = [
  "Transform negative thinking into positive energy",
  "Develop resilience and mental strength",
  "Create a personalized positive thinking practice",
  "Learn techniques from certified coaches",
  "Join a supportive community"
];

const AboutSection = () => {
  return (
    <section id="about" className="py-20 relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute bottom-40 right-1/4 w-72 h-72 bg-secondary/10 rounded-full blur-[100px]"></div>
        <div className="absolute top-20 left-1/4 w-72 h-72 bg-accent/10 rounded-full blur-[100px]"></div>
      </div>
      
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
          {/* About Content */}
          <div className="order-2 md:order-1">
            <Badge variant="ghost" className="mb-4">
              About Str8Positive
            </Badge>
            
            <h2 className="text-3xl md:text-4xl font-bold mb-6">
              Your Guide to a <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">Positive Mindset</span>
            </h2>
            
            <p className="text-muted-foreground mb-6">
              Str8Positive was founded with a simple mission: to help people transform their lives
              through the power of positive thinking. Our founder experienced firsthand how
              changing thought patterns can lead to extraordinary life changes.
            </p>
            
            <div className="space-y-4 mb-8">
              {aboutPoints.map((point, index) => (
                <div key={index} className="flex items-start gap-3">
                  <div className="relative flex-shrink-0 mt-1">
                    <div className="absolute inset-0 bg-primary/20 rounded-full blur-sm"></div>
                    <div className="relative">
                      <CheckCircle className="h-5 w-5 text-primary" />
                    </div>
                  </div>
                  <p className="text-foreground">{point}</p>
                </div>
              ))}
            </div>
            
            <div className="inline-flex items-center text-sm text-muted-foreground">
              <Sparkles className="h-4 w-4 text-primary mr-2" />
              Helping thousands transform their lives since 2015
            </div>
          </div>
          
          {/* Visual Element */}
          <div className="order-1 md:order-2">
            <div className="relative">
              <div className="absolute -inset-4 bg-gradient-to-r from-primary/20 via-secondary/20 to-accent/20 rounded-2xl blur-xl"></div>
              
              <div className="relative rounded-xl overflow-hidden">
                <div className="aspect-w-4 aspect-h-3 w-full">
                  <div className="bg-muted rounded-xl p-8 border border-primary/30 h-full backdrop-blur-sm">
                    <div className="h-full flex flex-col justify-center items-center space-y-8">
                      {/* Glowing orb */}
                      <div className="relative">
                        <div className="absolute inset-0 rounded-full bg-gradient-to-r from-primary/80 to-accent/80 blur-xl animate-pulse"></div>
                        <div className="relative w-24 h-24 rounded-full bg-gradient-to-r from-primary to-accent flex items-center justify-center">
                          <Sparkles className="h-10 w-10 text-white" />
                        </div>
                      </div>
                      
                      <div className="text-center">
                        <h3 className="text-xl font-bold mb-2">Our Mission</h3>
                        <p className="text-muted-foreground">
                          Empower individuals to transform their mindset and achieve their fullest potential
                          through proven positive thinking techniques.
                        </p>
                      </div>
                      
                      <div className="grid grid-cols-3 w-full gap-3 mt-4">
                        <div className="bg-card rounded-lg p-3 text-center">
                          <div className="text-2xl font-bold text-primary">10k+</div>
                          <div className="text-xs text-muted-foreground">Students</div>
                        </div>
                        <div className="bg-card rounded-lg p-3 text-center">
                          <div className="text-2xl font-bold text-secondary">24</div>
                          <div className="text-xs text-muted-foreground">Coaches</div>
                        </div>
                        <div className="bg-card rounded-lg p-3 text-center">
                          <div className="text-2xl font-bold text-accent">8</div>
                          <div className="text-xs text-muted-foreground">Years</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;