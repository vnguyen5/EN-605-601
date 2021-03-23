import React, { useState, useCallback, useMemo, useRef } from "react";
import { Col, Container, Form, Row } from "react-bootstrap";

export interface MessageInterface {
  type: string;
  message: string;
  action: string;
}
interface CluelessInterface {
  messages: MessageInterface[];
  onStart: () => void;
  onMove: () => void;
  onMakeSuggestion: () => void;
  onAccuse: () => void;
  onQuit: () => void;
}
export const Clueless = (props: CluelessInterface) => {
  const {
    messages,
    onStart,
    onMakeSuggestion,
    onMove,
    onAccuse,
    onQuit,
  } = props;
  React.useEffect(() => {});

  const parseMessages = (): string => {
    let output = "";

    messages.map((message) => {
      if (message.message) output += message.message + "\n";
    });
    return output;
  };
  return (
    <Container>
      <Row>
        <Col xs={12}>
          <Form className="col-xs-12">
            <Form.Group controlId="exampleForm.ControlTextarea1">
              <Form className="col-xs-12">
                <Form.Label>Message outputs</Form.Label>
              </Form>
              <Form className="col-xs-12">
                <textarea
                  style={{ width: "600px" }}
                  rows={20}
                  value={parseMessages()}
                  disabled={true}
                ></textarea>
              </Form>
            </Form.Group>
          </Form>
        </Col>
        <Col xs={12}>
          <button
            type="button"
            className="btn btn-success mr-1"
            onClick={onStart}
          >
            Start Game
          </button>
          <button
            type="button"
            className="btn btn-primary mr-1"
            onClick={onMove}
          >
            Move
          </button>
          <button
            type="button"
            className="btn btn-primary mr-1"
            onClick={onMakeSuggestion}
          >
            Make Suggestion
          </button>
          <button
            type="button"
            className="btn btn-danger mr-1"
            onClick={onAccuse}
          >
            Accuse
          </button>
          <button
            type="button"
            className="btn btn-warning mr-1"
            onClick={onQuit}
          >
            Quit
          </button>
        </Col>
      </Row>
    </Container>
  );
};
