import React from 'react';
import { Brain, Heart, Sun, Sparkles, Users, BookOpen, Medal, BarChart } from 'lucide-react';

const featureItems = [
  {
    icon: <Brain className="h-10 w-10 text-secondary" />,
    title: "Mindset Coaching",
    description: "One-on-one sessions with certified positive thinking coaches to rewire your thought patterns."
  },
  {
    icon: <Heart className="h-10 w-10 text-accent" />,
    title: "Wellness Programs",
    description: "Holistic approaches to mental and emotional wellbeing through positive thinking practices."
  },
  {
    icon: <Users className="h-10 w-10 text-primary" />,
    title: "Community Support",
    description: "Join our community of positive thinkers for encouragement, accountability, and friendship."
  },
  {
    icon: <BookOpen className="h-10 w-10 text-secondary" />,
    title: "Exclusive Resources",
    description: "Access to our library of eBooks, courses, and worksheets focused on positive thinking."
  },
  {
    icon: <Medal className="h-10 w-10 text-accent" />,
    title: "Success Stories",
    description: "Real-life transformations from people who have embraced the power of positive thinking."
  },
  {
    icon: <BarChart className="h-10 w-10 text-primary" />,
    title: "Progress Tracking",
    description: "Track your positive thinking journey with our specialized tools and metrics."
  }
];

const Features = () => {
  return (
    <section id="services" className="py-16 bg-gradient-to-b from-background to-muted">
      <div className="container px-4 md:px-6">
        <div className="flex flex-col items-center text-center space-y-4 mb-12">
          <div className="inline-block rounded-full bg-secondary/10 px-3 py-1 text-sm font-medium text-secondary">
            <span className="flex items-center gap-1">
              <Sparkles className="h-4 w-4" /> Our Services
            </span>
          </div>
          <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">
            Transforming Lives Through <span className="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">Positive Thinking</span>
          </h2>
          <p className="max-w-[700px] text-muted-foreground md:text-lg">
            We offer comprehensive services designed to help you cultivate a positive mindset and transform every aspect of your life.
          </p>
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {featureItems.map((feature, index) => (
            <div 
              key={index} 
              className="flex flex-col items-start p-6 rounded-xl bg-white border border-border shadow-sm transition-all hover:shadow-md"
            >
              <div className="rounded-full p-3 bg-muted mb-4">
                {feature.icon}
              </div>
              <h3 className="text-xl font-bold mb-2">{feature.title}</h3>
              <p className="text-muted-foreground">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;