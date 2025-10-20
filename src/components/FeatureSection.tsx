import React from "react";
import { Badge } from "@/components/ui/badge";
import { Brain, Heart, Users, BookOpen, WandSparkles, BarChart } from "lucide-react";

const features = [
  {
    icon: <Brain className="h-10 w-10" />,
    title: "Mindset Coaching",
    description: "One-on-one sessions with certified positive thinking coaches to rewire thought patterns.",
    gradient: "from-primary/80 to-primary/20",
    highlightGradient: "from-primary/20 to-transparent"
  },
  {
    icon: <WandSparkles className="h-10 w-10" />,
    title: "Transformation Tools",
    description: "Practical techniques and exercises to shift your thinking from negative to positive.",
    gradient: "from-secondary/80 to-secondary/20",
    highlightGradient: "from-secondary/20 to-transparent"
  },
  {
    icon: <Users className="h-10 w-10" />,
    title: "Community Support",
    description: "Join our community of positive thinkers for encouragement and accountability.",
    gradient: "from-accent/80 to-accent/20",
    highlightGradient: "from-accent/20 to-transparent"
  },
  {
    icon: <BookOpen className="h-10 w-10" />,
    title: "Exclusive Resources",
    description: "Access our library of eBooks, courses, and worksheets focused on positive thinking.",
    gradient: "from-primary/80 to-primary/20",
    highlightGradient: "from-primary/20 to-transparent"
  },
  {
    icon: <Heart className="h-10 w-10" />,
    title: "Wellness Programs",
    description: "Holistic approaches to mental and emotional wellbeing through positive practices.",
    gradient: "from-secondary/80 to-secondary/20",
    highlightGradient: "from-secondary/20 to-transparent"
  },
  {
    icon: <BarChart className="h-10 w-10" />,
    title: "Progress Tracking",
    description: "Track your positive thinking journey with specialized tools and metrics.",
    gradient: "from-accent/80 to-accent/20",
    highlightGradient: "from-accent/20 to-transparent"
  }
];

const FeatureSection = () => {
  return (
    <section id="services" className="py-20 relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute top-40 right-20 w-72 h-72 bg-primary/10 rounded-full blur-[100px]"></div>
        <div className="absolute bottom-20 left-20 w-72 h-72 bg-secondary/10 rounded-full blur-[100px]"></div>
      </div>
      
      <div className="container mx-auto px-4">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <Badge variant="ghost" className="mb-4">
            Our Services
          </Badge>
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            Transform Your Life Through <span className="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">Positive Thinking</span>
          </h2>
          <p className="text-muted-foreground">
            We offer comprehensive services designed to help you cultivate a positive mindset
            and transform every aspect of your life.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <div 
              key={index}
              className="relative group"
            >
              <div className="absolute -inset-2 rounded-xl bg-gradient-to-r from-primary/10 via-secondary/10 to-accent/10 opacity-0 group-hover:opacity-100 blur-xl transition-all duration-300"></div>
              <div className="relative bg-card border border-primary/10 rounded-xl p-8 h-full backdrop-blur-sm transition-all duration-300 hover:border-primary/30">
                <div className="flex flex-col h-full">
                  <div className="mb-6 relative">
                    <div className={`absolute inset-0 rounded-lg bg-gradient-to-br ${feature.gradient} opacity-20`}></div>
                    <div className="relative p-4 w-fit rounded-lg">
                      {feature.icon}
                    </div>
                  </div>
                  <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
                  <p className="text-muted-foreground text-sm mb-4">{feature.description}</p>
                  
                  <div className="mt-auto pt-6 relative overflow-hidden rounded-lg">
                    <div className={`absolute inset-0 bg-gradient-to-r ${feature.highlightGradient} opacity-0 group-hover:opacity-100 transition-opacity duration-300`}></div>
                    <div className="h-1 w-12 bg-gradient-to-r from-primary to-secondary rounded-full"></div>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeatureSection;