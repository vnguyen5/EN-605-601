import React, { useState, useCallback, useMemo, useRef } from "react";
import { Col, Container, Form, Row } from "react-bootstrap";

export interface MessageInterface {
  type: string;
  message?: string;
  action: string;
  weapon?: string;
  suspect?: string;
  roomNumber?: number;
  room?: string;
}
interface CluelessInterface {
  messages: MessageInterface[];
  onStart: () => void;
  onMove: (roomNumber?: number) => void;
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
    <React.Fragment>
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
              onClick={() => onMove(-1)}
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
      <br />
      <Container>
        <Row>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(1)}
              style={{ width: "150px" }}
            >
              Study
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(6)}
            >
              {"--------------------"}
              <br />
              {"--------------------"}
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(9)}
              style={{ width: "150px" }}
            >
              Hall
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(14)}
            >
              {"--------------------"}
              <br />
              {"--------------------"}
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(17)}
              style={{ width: "150px" }}
            >
              Lounge
            </button>
          </Col>
        </Row>
        <Row>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(2)}
            >
              {"|  |"}
              <br />
              {"|  |"}
              <br />
              {"|  |"}
            </button>
          </Col>
          <Col xs={2} />
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(10)}
            >
              {"|  |"}
              <br />
              {"|  |"}
              <br />
              {"|  |"}
            </button>
          </Col>
          <Col xs={2} />
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(18)}
            >
              {"|  |"}
              <br />
              {"|  |"}
              <br />
              {"|  |"}
            </button>
          </Col>
        </Row>
        <Row>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(3)}
              style={{ width: "150px" }}
            >
              Library
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(7)}
            >
              {"--------------------"}
              <br />
              {"--------------------"}
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(11)}
              style={{ width: "150px" }}
            >
              Billard Room
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(15)}
            >
              {"--------------------"}
              <br />
              {"--------------------"}
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(19)}
              style={{ width: "150px" }}
            >
              Dinnig Room
            </button>
          </Col>
        </Row>
        <Row>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(4)}
            >
              {"|  |"}
              <br />
              {"|  |"}
              <br />
              {"|  |"}
            </button>
          </Col>
          <Col xs={2} />
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(12)}
            >
              {"|  |"}
              <br />
              {"|  |"}
              <br />
              {"|  |"}
            </button>
          </Col>
          <Col xs={2} />
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(20)}
            >
              {"|  |"}
              <br />
              {"|  |"}
              <br />
              {"|  |"}
            </button>
          </Col>
        </Row>
        <Row>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(5)}
              style={{ width: "150px" }}
            >
              Conservatory
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(8)}
            >
              {"--------------------"}
              <br />
              {"--------------------"}
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(13)}
              style={{ width: "150px" }}
            >
              Ballroom
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-info mr-1 btn-sm"
              onClick={() => onMove(16)}
            >
              {"--------------------"}
              <br />
              {"--------------------"}
            </button>
          </Col>
          <Col xs={2}>
            <button
              type="button"
              className="btn btn-success mr-1 btn-lg"
              onClick={() => onMove(21)}
              style={{ width: "150px" }}
            >
              Kitchen
            </button>
          </Col>
        </Row>
      </Container>
    </React.Fragment>
  );
};
