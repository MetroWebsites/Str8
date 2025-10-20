import React, { useState } from "react";
import { Button } from "./ui/button";
import { Send } from "lucide-react";

export default function ContactForm() {
  const defaultFormData = {name: "", email: "", message: "", form_name: "Positive Thinking Inquiry"};
  const [formData, setFormData] = useState(defaultFormData);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<"success" | "error" | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setSubmitStatus(null);

    try {
      const response = await fetch("https://api.new.website/api/submit-form/", {
        method: "POST",
        headers: {
          "Content-Type": "multipart/form-data",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setSubmitStatus("success");
        setFormData(defaultFormData);
      } else {
        setSubmitStatus("error");
      }
    } catch (error) {
      setSubmitStatus("error");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div id="contact" className="w-full max-w-md mx-auto mt-8">
      <h2 className="text-2xl font-bold mb-6">Get in Touch</h2>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="name" className="block text-sm font-medium mb-1">
            Name
          </label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            required
            className="w-full px-4 py-2 bg-muted/50 border border-primary/10 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50"
            placeholder="Your name"
          />
        </div>

        <div>
          <label htmlFor="email" className="block text-sm font-medium mb-1">
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            required
            className="w-full px-4 py-2 bg-muted/50 border border-primary/10 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50"
            placeholder="your.email@example.com"
          />
        </div>

        <div>
          <label htmlFor="message" className="block text-sm font-medium mb-1">
            Message
          </label>
          <textarea
            id="message"
            name="message"
            value={formData.message}
            onChange={handleInputChange}
            required
            rows={4}
            className="w-full px-4 py-2 bg-muted/50 border border-primary/10 rounded-md focus:outline-none focus:ring-2 focus:ring-primary/50"
            placeholder="How can we help you with positive thinking?"
          />
        </div>

        <input name="form_name" type="hidden" value={formData.form_name} />
        
        <Button
          type="submit"
          disabled={isSubmitting}
          className="w-full"
        >
          {isSubmitting ? "Submitting..." : (
            <span className="flex items-center gap-2">
              Send Message <Send className="h-4 w-4" />
            </span>
          )}
        </Button>

        {submitStatus === "success" && (
          <div className="p-4 bg-accent/20 border border-accent/30 rounded-md">
            Thank you for reaching out! We'll be in touch soon.
          </div>
        )}

        {submitStatus === "error" && (
          <div className="p-4 bg-destructive/20 border border-destructive/30 rounded-md">
            There was an error submitting the form. Please try again.
          </div>
        )}
      </form>
    </div>
  );
}